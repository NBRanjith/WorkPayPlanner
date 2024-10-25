import math

class Days:
    def __init__(self, pay_rate, hours=10):
        self.pay_rate = pay_rate
        self.hours = hours
        self.net_pay_sp = self.calculate_over_time_pay_sp()
        self.net_pay_wp = self.calculate_over_time_pay_wp()

    def calculate_over_time_pay_sp(self):
        gross_pay = self.hours * self.pay_rate * 1.5  # Overtime pay
        tax_ot = (13 / 100) * gross_pay
        net_pay_sp = gross_pay - tax_ot
        return net_pay_sp

    def calculate_over_time_pay_wp(self):
        gross_pay = self.hours * self.pay_rate * 1.5  # Overtime pay
        tax_ot = (19.79 / 100) * gross_pay
        net_pay_wp = gross_pay - tax_ot
        return net_pay_wp

    def budget_goal_days(self, required_amount, net_pay):
        days = required_amount / net_pay
        return math.ceil(days), days


class AmazonPay:
    def __init__(self, weekly_pay=0, hourly_rate=22.10, symbol='$', hours=40, sp_taxes=13, wp_taxes=19.79):
        self.hourly_rate = hourly_rate
        self.symbol = symbol
        self.hours = hours
        self.sp_taxes = sp_taxes
        self.wp_taxes = wp_taxes
        self.weekly_pay = weekly_pay

    def __repr__(self):
        return f'{self.symbol}{self.weekly_pay:,.2f}'

    def show_weekly_sal_sp(self):
        gross_pay = self.hours * self.hourly_rate
        tax_amount = (self.sp_taxes / 100) * gross_pay
        net_pay = gross_pay - tax_amount
        self.weekly_pay = net_pay
        return net_pay

    def show_weekly_sal_wp(self):
        gross_pay = self.hours * self.hourly_rate
        tax_amount = (self.wp_taxes / 100) * gross_pay
        net_pay = gross_pay - tax_amount
        self.weekly_pay = net_pay
        return net_pay


name = input('Enter your name: ')
status = ''
while status not in ['sp', 'wp']:
    status = input('Are you on sp (Study Permit) or wp (Work Permit)? (sp/wp only): ').strip().lower()

choice = ''
while choice not in ['goal', 'earnings']:
    choice = input(
        'Do you want to calculate based on a budget goal or see your daily overtime earnings? (goal/earnings): ').strip().lower()

if choice == 'goal':
    pay_rate = float(input('Enter your hourly pay rate: '))
    while True:
        try:
            hours = float(input('Enter the number of hours you work overtime per day: '))
            if hours > 0:
                break
        except ValueError:
            print("Please enter a valid number for overtime hours.")

    num_days = Days(pay_rate, hours)
    budget_goal = float(input('Enter your budget goal amount: '))

    if status == 'sp':
        days_needed, exact_days = num_days.budget_goal_days(budget_goal, num_days.net_pay_sp)
        print(
            f"Days needed to work: {days_needed} days (exact: {exact_days:.2f}). You will earn: {num_days.net_pay_sp:.2f} per day.")
        print(f"Total for {days_needed} days: {num_days.net_pay_sp * days_needed:.2f}")
    elif status == 'wp':
        days_needed, exact_days = num_days.budget_goal_days(budget_goal, num_days.net_pay_wp)
        print(
            f"Days needed to work: {days_needed} days (exact: {exact_days:.2f}). You will earn: {num_days.net_pay_wp:.2f} per day.")
        print(f"Total for {days_needed} days: {num_days.net_pay_wp * days_needed:.2f}")

elif choice == 'earnings':
    pay_rate = float(input('Enter your hourly pay rate: '))
    while True:
        try:
            hours = float(input('Enter the number of hours you worked: '))
            if hours > 0:
                break
        except ValueError:
            print("Please enter a valid number for hours worked.")

    num_days = Days(pay_rate, hours)

    if status == 'sp':
        print(f"Study Permit daily overtime earnings: {num_days.net_pay_sp:.2f}")
    elif status == 'wp':
        print(f"Work Permit daily overtime earnings: {num_days.net_pay_wp:.2f}")
