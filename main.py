import click
import requests
import os
from typing import List, Optional

FILENAME = 'urls.csv'

@click.group()
def cli() -> None:
  pass

@cli.command()
def run() -> None:
  try:
    with open(FILENAME, 'r') as file :
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
    except requests.exceptions.MissingSchema:
      click.echo(f'URL: {url} -> Status: Wrong URL, Perhaps you want add https://')   

@cli.command()
@click.argument('url', required=False)
@click.option('--all', '-a', is_flag=True, help='to delete all urls')
def remove(url: str, all:bool) -> None:
  try:
    with open(FILENAME, 'r') as file :
      filedata = file.read()
  except FileNotFoundError:
    click.echo('There is no File, please add one URL')
    return

  if all:
    os.remove("urls.csv")
    click.echo('All URLs removed with success')
    return

  filelist: List[str] = filedata.split(",\n")
  if url not in filelist:
    click.echo('URL not found')
    return

  filedata = filedata.replace(url + ",\n", '')

  with open(FILENAME, 'w') as file:
    file.write(filedata)
    click.echo('URL removed with success')

@cli.command()
@click.argument('url')
def add(url: str) -> None:
  try:
    with open(FILENAME, 'r') as file :
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

@cli.command()
def urls() -> None:
  try:
    with open(FILENAME, 'r') as file :
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
    click.echo(url)

if __name__ == '__main__':
  cli()