from fastcli import FastCLI, Router

cli = FastCLI()

artists_router = Router()

@artists_router.register('')
def list_artists():
    return 'This is where there would be a list of artists'

@artists_router.register('add')
def add_artist():
    return 'This is where you add an artist'

@artists_router.register('delete')
def delete_artist():
    return 'This is where you delete an artist'


cli.include_router('artists', artists_router)

@cli.register('albums')
def read_albums():
    return "This is a list of albums"

cli.run()
