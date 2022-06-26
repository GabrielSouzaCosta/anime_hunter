from django import template

register = template.Library()

@register.filter
def in_tier(animes, tier_rating):
    return animes.filter(tier_rating=tier_rating)

@register.filter
def not_watching(animes):
    animes = animes.filter(watching=False, watched=False)
    if animes:
        return animes
    else:
        return None
    
@register.filter
def watching(animes):
    animes = animes.filter(watching=True, watched=False)
    if animes:
        return animes
    else:
        return None

@register.filter
def watched(animes):
    animes = animes.filter(watching=False, watched=True)
    if animes:
        return animes
    else:
        return None

