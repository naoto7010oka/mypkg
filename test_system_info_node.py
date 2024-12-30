import pytest
from datetime import datetime
import psutil

def test_time_format():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    assert isinstance(now, str)
    assert len(now) == 19

def test_battery_info():
    battery = psutil.sensors_battery()
    if battery is not None:
        assert 0 <= battery.percent <= 100
        assert isinstance(battery.power_plugged, bool)
    else:
        assert battery is None

