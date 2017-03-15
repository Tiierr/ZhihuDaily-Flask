# Added at : 2017.03.10
# Author   : RayYu03
# Usage    : A utility class provide datetime function.

from datetime import datetime, timedelta

__all__ = ['Datetime']

class Datetime(object):
    def __init__(self):
        """
        Initialize the time.
        """
        self._time = self.today + timedelta(1)

    @property
    def today(self):
        return datetime.now()

    @property
    def now(self):
        return self._time.strftime('%Y%m%d')

    @property
    def current(self):
        return self.today.strftime('%Y%m%d')

    @property
    def yesterday(self):
        return (self._time + timedelta(-1)).strftime('%Y%m%d')

    @property
    def tomorrow(self):
        return (self._time + timedelta(1)).strftime('%Y%m%d')

    def before(self, days):
        return (self._time + timedelta(-days)).strftime('%Y%m%d')

    def after(self, days):
        return (self._time + timedelta(days)).strftime('%Y%m%d')

    def __str__(self):
        return self._time.strftime('%Y%m%d')

if __name__ == '__main__':
    date = Date()
    print(date.now)
    print(date.yesterday)
    print(date.before(5))
    print(date)
