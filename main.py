import click
import requests
from typing import List, Optional

@click.group()
def cli() -> None:
    pass

@cli.command()
def run() -> None:
  try:
    with open('urls.csv', 'r') as file :
      filedata = file.read()
  except FileNotFoundError:
    click.echo('There is no File, please add one URL')
    return

  if not filedata:
    click.echo('There is no URL, please add one')
    return

  filelist: List[str] = filedata.split(",\n")

  for url in filelist:
    if url == '':
      continue
    try:
      status = requests.head(url).status_code
      click.echo(f'URL: {url} -> Status: {status}')
    except requests.exceptions.ConnectionError:
      click.echo(f'URL: {url} -> Status: URL not reachable')   

@cli.command()
@click.argument('url')
def remove(url: str) -> None:
  try:
    with open('urls.csv', 'r') as file :
      filedata = file.read()
  except FileNotFoundError:
    click.echo('There is no File, please add one URL')
    return

  filelist: List[str] = filedata.split(",\n")
  if url not in filelist:
    click.echo('URL not found')
    return

  filedata = filedata.replace(url + ",\n", '')

  with open('urls.csv', 'w') as file:
    file.write(filedata)
    click.echo('URL removed with success')

@cli.command()
@click.argument('url')
def add(url: str) -> None:
  try:
    with open('urls.csv', 'r') as file :
      filedata = file.read()
  except FileNotFoundError:
    with open("urls.csv", "a") as f:
      f.write(url + ",\n")
    click.echo('URL Added with Success')
    return

  filelist: List[str] = filedata.split(",\n")
  if url in filelist:
    click.echo('URL already exists')
    return

  with open("urls.csv", "a") as f:
    f.write(url + ",\n")
  click.echo('URL Added with Success')

if __name__ == '__main__':
  cli()