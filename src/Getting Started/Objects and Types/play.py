import tkinter as tk
import tkcalendar as tkc
import calendar


class MyCalendar(tkc.Calendar):
    def __init__(self, master=None,
                 allowed_weekdays=(calendar.MONDAY, calendar.TUESDAY, calendar.WEDNESDAY, calendar.THURSDAY), **kw):
        self._select_only = allowed_weekdays
        tkc.Calendar.__init__(self, master, **kw)
        # change initially selected day if not right day
        if self._sel_date and not (self._sel_date.isoweekday() - 1) in allowed_weekdays:
            year, week, wday = self._sel_date.isocalendar()
            # get closest weekday
            next_wday = max(allowed_weekdays, key=lambda d: (d - wday + 1) > 0) + 1
            sel_date = self.date.fromisocalendar(year, week + int(next_wday < wday), next_wday)
            self.selection_set(sel_date)

    def _display_calendar(self):
        # display calendar
        tkc.Calendar._display_calendar(self)
        # disable not allowed days
        for i in range(6):
            for j in range(7):
                if j in (calendar.MONDAY, calendar.TUESDAY, calendar.WEDNESDAY, calendar.THURSDAY,calendar.SUNDAY) :
                    continue
                self._calendar[i][j].state(['disabled'])
        # list l=[1]
        # print(self._calendar.index([1],12))


root = tk.Tk()
cal = MyCalendar(root, allowed_weekdays=(calendar.WEDNESDAY, calendar.SATURDAY),
                 weekendbackground='white', weekendforeground='black',
                 othermonthbackground='gray95', othermonthwebackground='gray95',
                 othermonthforeground='black', othermonthweforeground='black')
cal.pack()
root.mainloop()
