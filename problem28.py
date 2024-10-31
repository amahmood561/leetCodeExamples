'''
Prorating Subscriptions
Background
Our company has started selling to larger customers, so we are creating subscription tiers with different feature sets to cater to our customers’ unique needs. We previously charged every customer a flat fee per month, but now we plan on charging for the number of users active on the customer's subscription plan. As a result, we're changing our billing system.

Instructions
You’ve picked up the work item to implement the logic to compute the monthly charge:

Prorating Subscriptions (#8675309)
We'd like you to implement a monthly_charge function to calculate the total monthly bill for a customer.

Customers are billed based on their subscription tier. We charge them a prorated amount for the portion of the month each user’s subscription was active. For example, if a user was activated or deactivated part way through the month, then we charge them only for the days their subscription was active.

We want to bill customers for all days users were active in the month (including any activation and deactivation dates, since the user had some access on those days).

We do need to support historical calculations (previous dates)
We only charge whole cents
Notes
Here’s an idea of how we might go about this:

Calculate a daily rate for the subscription tier
For each day of the month, identify which users had an active subscription on that day
Multiply the number of active users for the day by the daily rate to calculate the total for the day
Return the running total for the month at the end
Testing
The provided unit tests only cover a few cases that one of your colleagues shared, so you should plan to add your own tests to ensure that your solution handles any edge cases.

Notes
It’s more important for the return value to be correct than it is for the algorithm to be highly optimized.
You should not change function names or return types of the provided functions since our test cases depend on those not changing.

'''

import datetime
import calendar

def monthly_charge(month, subscription, users):
    # Edge case: No subscription or no active users
    if not subscription or not users:
        return 0
    
    # Parse the month to get the first and last day of the month
    year, month = map(int, month.split("-"))
    first_day = datetime.date(year, month, 1)
    last_day = datetime.date(year, month, calendar.monthrange(year, month)[1])
    
    # Calculate daily rate (in cents)
    daily_rate = subscription['monthly_price_in_cents'] / last_day.day

    total_charge = 0

    # Iterate through each day of the month
    current_day = first_day
    while current_day <= last_day:
        # Count active users for the current day
        active_user_count = sum(
            1 for user in users
            if (user['activated_on'] <= current_day) and 
               (user['deactivated_on'] is None or user['deactivated_on'] >= current_day)
        )
        
        # Add daily charge for active users
        total_charge += active_user_count * daily_rate
        current_day = next_day(current_day)
    
    # Round to the nearest cent
    return round(total_charge)

####################
# Helper functions #
####################

def first_day_of_month(date):
    return date.replace(day=1)

def last_day_of_month(date):
    last_day = calendar.monthrange(date.year, date.month)[1]
    return date.replace(day=last_day)

def next_day(date):
    return date + datetime.timedelta(days=1)
