from django.dispatch import Signal

"""
These signals are different from IPN signals in that they are sent the second
the payment is failed or succeeds and come with the `item` object passed to
PayPalPro rather than an IPN object.
"""

# Sent when a recurring payments profile is created.
payment_profile_created = Signal(providing_args=['nvp_obj', 'params', 'request'])

# Sent when a payment is successfully processed.
payment_was_successful = Signal(providing_args=['nvp_obj', 'params', 'request'])

# Sent when a payment is flagged.
payment_was_flagged = Signal(providing_args=['nvp_obj', 'params', 'request'])

# Sent when user cancels their own recurring profile
recurring_cancel = Signal(providing_args=['nvp_obj', 'params', 'request'])

# Sent when user suspends their own profile
recurring_suspend = Signal(providing_args=['nvp_obj', 'params', 'request'])

# Send when user reactivates their own profile
recurring_reactivate = Signal(providing_args=['nvp_obj', 'params', 'request'])