import click

from .phonebook import Phonebook

pb = Phonebook()

@click.group()
def cli():
    pass

@cli.command(help='Queries the phonebook.')
@click.argument('qs', required=False)
# @cli.option('-i', '--case-insensitive',
#             help='Performs a case-insensitive search.')
def query(qs):
    if qs:
        results = set()
        results.update(pb.query_name(qs))
        results.update(pb.query_phone(qs))
    else:
        results = pb.get_all()

    for r in results:
        print(r)


if __name__ == '__main__':
    cli()