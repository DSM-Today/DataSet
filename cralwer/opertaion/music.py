from requests import get

from random import randint
from typing import Optional


def generate_random_int(maximum: int, minimum: Optional[int] = None):
    minimum = 1 if minimum is None else minimum
    return randint(minimum, maximum)


class Music:

    def __init__(self):
        situation_id_list = [1, 4, 11, 12, 2, 13, 5, 6, 14, 15, 3, 17, 18, 19, 10, 122, 123]
        situation_name_list = ['드라이브', '공부/독서', '사랑', '이별', '운동/헬스', '산책/여행', '아침', '밤/새벽', '카페', '휴식/힐링', '출/퇴근',
                               '혼술/혼밥', '내 방', '노래방', '호텔/라운지', '펍/바', '일/작업']
        random_int = generate_random_int(len(situation_name_list) - 1)

        self._situation = situation_name_list[random_int]
        self._situation_id = situation_id_list[random_int]

    def crawl(self):

        channel_id = self._get_random_playlist_id()

        playlist_detail = self._get_playlist_detail(channel_id)

        return self._parse_playlist_detail(playlist_detail)

    def _get_random_playlist_id(self) -> int:
        channel_list = get(
            f'https://www.music-flo.com/api/display/v1/browser/SITTN/{self._situation_id}?sortType=RECOMMEND'
        ).json()['data']['chnlList']

        random_int = generate_random_int(len(channel_list))

        return channel_list[random_int]['id']

    @staticmethod
    def _get_playlist_detail(playlist_id: int) -> dict:
        return get(
            f'https://www.music-flo.com/api/meta/v1/channel/{playlist_id}'
        ).json()['data']

    def _parse_playlist_detail(self, playlist_detail: dict):
        random_int = generate_random_int(playlist_detail['trackCount'] - 1)
        track = playlist_detail['trackList'][random_int]
        return {
            'situation': self._situation,
            'playlist_provider': playlist_detail['creator']['name'],
            'playlist_direct_url': f"https://www.music-flo.com/search/theme?keyword={playlist_detail['name']}&sortType=ACCURACY",
            'is_adult': True if track['adultAuthYn'] == 'Y' else False,
            'image_path': track['album']['imgList'][2]['url'],
            'album_name': track['album']['title'],
            'released_at': track['album']['releaseYmd'],
            'title': track['name'],
            'play_time': track['playTime'],
            'song_writer': track['representationArtist']['name']
        }
