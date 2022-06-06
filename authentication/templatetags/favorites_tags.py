from django import template

register = template.Library()

@register.filter
def in_tier(animes, tier_rating):
    return animes.filter(tier_rating=tier_rating)