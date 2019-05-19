import sys

import click

from api.google import GoogleTranslator
from api.weblio import WeblioTranslator


_translators = {
    'google': GoogleTranslator,
    'weblio': WeblioTranslator,
}


@click.command()
@click.option('--text')
@click.option('--from', 'source')
@click.option('--to', 'target')
@click.option('--api', default='weblio')
def main(text, source, target, api):
    if api not in _translators:
        print('Error: API "%s" is not supported.' % api)
        sys.exit(1)
    print(_translators[api]().translate(text, source, target))


if __name__ == '__main__':
    main()


# EOF
