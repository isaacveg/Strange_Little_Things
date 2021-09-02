import json
from os.path import join
from datetime import timedelta
from datetime import datetime

def draft_content_to_tracks(draft_content: json) -> list:
    texts = {t['id']: t['content']
             for t in draft_content['materials']['texts']
             if t['type'] == 'subtitle'}

    """[
        'start': (μs),
        'end': (μs),
        'content': (...)
    }]"""
    tracks = []
    for t in draft_content['tracks']:
        for s in t['segments']:
            if s['material_id'] in texts.keys():
                timerange = s['target_timerange']
                tracks.append({
                    'start': timerange['start'],
                    'end': timerange['start'] + timerange['duration'],
                    'content': texts[s['material_id']]
                })

    return tracks

def us_to_string(microseconds):
    return (datetime(1, 1, 1) + timedelta(microseconds=microseconds)).strftime('%H:%M:%S') + ',' + str((microseconds % 10**6) // 10**3).zfill(3)


def tracks_to_srt_list(tracks):
    tracks.sort(key=lambda t: t['start'])
    tracks_in_string = []
    for i, t in enumerate(tracks):
        tracks_in_string.append(
            '\n'.join([str(i),
                       us_to_string(t['start']) + ' --> ' +
                       us_to_string(t['end']),
                       t['content']])
        )

    return tracks_in_string


def tracks_to_srt_string(tracks):
    return '\n\n'.join(tracks_to_srt_list(tracks))

if __name__ == '__main__':
    raw_path = input("请输入你想要处理的文件路径，可以直接拖入输入框: ")
    raw_path = raw_path.replace("'","")
    try: 
        f = open(raw_path, 'r', encoding='utf-8')
        draft_content = json.load(f)
    except:
        print("没有这个文件，重新检查输入")
        exit(1)

    print("成功读入文件，开始解析...")
    tracks = draft_content_to_tracks(draft_content)
    subtitle_filename = "result.srt"
    with open(subtitle_filename, 'w', encoding='utf-8') as fp:
        fp.write(tracks_to_srt_string(tracks))

    print(f'请查收 result.txt。它应该出现在本 python 文件相同的目录中。')
    input('请按 Enter 继续. . .')
