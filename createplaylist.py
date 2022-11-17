import os
from spotifyclient import SpotifyClient

def main():
    cliente_spotify = SpotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
                                   os.getenv("SPOTIFY_USER_ID"))

    # get ultimas canciones reproducidas
    num_canciones_visualizadas = int(input("Cuantas canciones desea visualizar? "))
    ultimas_canciones_reproducidas = cliente_spotify.get_last_played_tracks(num_canciones_visualizadas)

    print(f"\nLas ultimas {num_canciones_visualizadas} canciones reproducidas en tu Spotify:")
    for index, track in enumerate(ultimas_canciones_reproducidas):
        print(f"{index+1}- {track}")

    # elige qué pistas usar como semilla para generar una lista de reproducción
    indexes = input("\nIngrese una lista de hasta 5 pistas que le gustaría usar como semillas: ")
    indexes = indexes.split()
    canciones_Semillas = [ultimas_canciones_reproducidas[int(index)-1] for index in indexes]

    # get pistas recomendadas basadas en pistas semilla
    canciones_recomendadas = cliente_spotify.get_track_recommendations(canciones_Semillas)
    print("\nEstas son las pistas recomendadas que se incluirán en su nueva playlist:")
    for index, track in enumerate(canciones_recomendadas):
        print(f"{index+1}- {track}")

    # get nombre de la lista de reproducción del usuario y crear lista de reproducción
    nombre_playlist = input("\nCual es el nombre de la playlist? ")
    playlist = cliente_spotify.create_playlist(nombre_playlist)
    print(f"\nLa playlist '{playlist.name}'fue creada exitosamente.")

    # llenar la lista de reproducción con pistas recomendadas
    cliente_spotify.populate_playlist(playlist, canciones_recomendadas)
    print(f"\nPistas recomendadas cargadas con éxito a la lista de reproducción '{playlist.name}'.")


if __name__ == "__main__":
    main()
