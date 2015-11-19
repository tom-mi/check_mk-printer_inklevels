import pytest

from pytest_check_mk import OK, WARNING, CRITICAL, UNKNOWN
from pytest_check_mk.assertions import assert_inventory_and_check_works_with_check_output


test_for = 'printer_inklevels'


check_output = '''
<<<printer_inklevels:sep(9)>>>
/dev/usb/lp0\tmodel\tWooden printing press
/dev/usb/lp0\tlevel\tBlack\t20
/dev/usb/lp0\tlevel\tColor\t53
/dev/666\tmodel\tEvil printing press
/dev/666\tlevel\tRed\t7
'''


@pytest.fixture
def check(checks):
    return checks['printer_inklevels']


def test_settings(check):
    assert check.has_perfdata
    assert check.service_description == 'Inklevels of %s'


def test_empty_inventory(check):
    assert check.inventory('<<<printer_inklevels:sep(9)>>>') == []


def test_inventory(check):
    assert check.inventory(check_output) == [
        ('/dev/usb/lp0', 'printer_inklevels_default_values'),
        ('/dev/666', 'printer_inklevels_default_values'),
    ]


def test_default_values(checks):
    assert checks.module.printer_inklevels_default_values == (10, 5)


def test_check_unknown_item(check):
    warn, critical = 10, 5
    assert check.check('/dev/foo/bar', (warn, critical), check_output) == (UNKNOWN, 'Unknown printer /dev/foo/bar')


def test_check_basic_output(check):
    warn, critical = 10, 5

    status, message, _ = check.check('/dev/usb/lp0', (warn, critical), check_output)
    assert status == OK
    assert message == 'Wooden printing press - Black: 20%, Color: 53%'

    status, message, _ = check.check('/dev/666', (warn, critical), check_output)
    assert status == WARNING
    assert message == 'Evil printing press - Red: 7%(!)'


@pytest.mark.parametrize('warn, critical, expected_status, expected_message', [
    (19, 18, OK,       'Wooden printing press - Black: 20%, Color: 53%'),
    (20, 18, WARNING,  'Wooden printing press - Black: 20%(!), Color: 53%'),
    (22, 20, CRITICAL, 'Wooden printing press - Black: 20%(!!), Color: 53%'),
    (53, 20, CRITICAL, 'Wooden printing press - Black: 20%(!!), Color: 53%(!)'),
])
def test_check_levels(check, warn, critical, expected_status, expected_message):
    status, message, _ = check.check('/dev/usb/lp0', (warn, critical), check_output)

    assert status == expected_status
    assert message == expected_message


def test_check_perfdata(check):
    warn, critical = 15, 13
    _, _, perfdata = check.check('/dev/usb/lp0', (warn, critical), check_output)

    assert perfdata == [
        ('Black', 20, warn, critical, 0, 100),
        ('Color', 53, warn, critical, 0, 100),
    ]


def test_consistency(check):
    assert_inventory_and_check_works_with_check_output(check, check_output)


def test_with_fake_agent_output(agents, check):
    assert_inventory_and_check_works_with_check_output(check, agents['plugins/printer_inklevels'].run('--fake-data'))


def test_empty_agent_output(agents):
    assert agents['plugins/printer_inklevels'].run('--fake-empty') == ''
