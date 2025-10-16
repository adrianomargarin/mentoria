from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def querystring(context, **kwargs):
    """
    Retorna "?chave=valor&..." preservando os parâmetros atuais do request,
    sobrescrevendo/adiocionando os passados em kwargs.
    """
    request = context['request']
    params = request.GET.copy()

    for k, v in kwargs.items():
        params[k] = v

    qs = params.urlencode()

    return f'?{qs}' if qs else '?'
