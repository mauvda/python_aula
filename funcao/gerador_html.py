#!usr/bin/python3
bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def get_args(argumentos, suporte):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in argumentos.items() if k in suporte)


def tag_bloco(conteudo, *args, classe='success', inline=False, **atributo):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **atributo)
    return f'<{tag} {get_args(atributo, bloco_atrs)} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **atributo):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul {get_args(atributo, ul_atrs)}>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe="info", inline=True,
                    bloco_accesskey="m", bloco_id="conteudo", ul_id="lista",
                    ul_style="color:red"))
