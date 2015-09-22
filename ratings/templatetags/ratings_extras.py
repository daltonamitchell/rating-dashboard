from django import template

register = template.Library()

@register.filter
def bootstrap_context(value, max_value):
    """
    Returns a Bootstrap contextual string based on the closeness to the max_value

    Args:
        value (int): Current value
        max_value (int): The maximum possible, used to determine a percentage

    Returns:
        (str): One of the following Bootstrap contextual strings:
               'primary', 'success', 'info', 'warning', 'danger'
    """
    percentage = value / max_value * 100

    if percentage >= 80:
        return 'primary'
    elif 80 > percentage and percentage >= 60:
        return 'success'
    elif 60 > percentage and percentage >= 40:
        return 'info'
    elif 40 > percentage and percentage >= 20:
        return 'warning'
    else:
        return 'danger'
