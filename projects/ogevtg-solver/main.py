import requests
import aiohttp
import asyncio

subjects = [
    {
	'name': 'inf',
	'types': [
    "inf-1",
    "inf-2",
    "inf-3",
    "inf-5",
    "inf-4",
    "inf-6",
    "inf-9",
    "inf-7",
    "inf-8",
    "inf-10",
    "inf-11",
    "inf-12",
    "inf-13.1",
    "inf-13.2",
    "inf-14",
    "inf-16",
    "inf-15",
]
    },
{
"name": "bio",
"types": 
[
    "bio-1",
    "bio-2",
    "bio-3",
    "bio-6",
    "bio-4",
    "bio-5",
    "bio-7",
    "bio-8",
    "bio-9",
    "bio-12",
    "bio-11",
    "bio-10",
    "bio-16",
    "bio-13",
    "bio-14",
    "bio-17",
    "bio-18",
    "bio-15",
"bio-19-21",
  "bio-22",
  "bio-23",
  "bio-24",
  "bio-26",
  "bio-25"
]
},

    {
        'name': 'mat', 
        'types':[
            'mat-derevnia',
            'mat-shina',
            'mat-uchastok',
            'mat-kvartira',
            'mat-sviaz',
            'mat-listi',
            'mat-derevni7',
            'mat-pechki',
            "mat-6",
            "mat-7",
            "mat-8",
            "mat-9",
            "mat-10",
            "mat-19",
            "mat-18",
            "mat-15",
            "mat-12",
            "mat-13",
            "mat-16",
            "mat-17",
            "mat-14",
            "mat-11",
            "mat-20",
            "mat-21",
            "mat-22",
            "mat-23",
            "mat-24",
            "mat-25"
        ]
    },
    {
        'name': 'rus',
        'types': [
            'rus-2-3',
            "rus-4", 
            "rus-5",
            "rus-6","rus-7", "rus-8", "rus-9",
            'rus-10-13',
        ]  
    }
]

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'http://ogevtg.ru',
    'Referer': 'http://ogevtg.ru/mat/mat-1-5/solve',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
}

async def solve_task(not_solved, session, task, subject):
    print('Taskid:', task['task_id'])
    print(task)
    is_group = task.get('is_group')
    if is_group:
        for sub_task in task['sub_tasks']:
            print('Sub task:', sub_task['task_id'])
            try:
                answer = sub_task['answer']
                if isinstance(answer, list):
                    answer = answer[0]
            except KeyError: return
            task_id = sub_task['task_id']
            task_type = sub_task['task_type']

            json_answer_data = {
                'subject': subject['name'],
                'task_id': task_id,
                'task_type': str(task_type),
                'user_answer': answer,
                'expected_answer': answer,
                'user_login': 'roca',
            }
    else:
        try:
            answer = task['answer']
            if isinstance(answer, list):
                answer = answer[0]
        except KeyError: return
        task_id = task['task_id']
        task_type = task['task_type']
        json_answer_data = {
            'subject': subject['name'],
            'task_id': task_id,
            'task_type': str(task_type),
            'user_answer': answer,
            'expected_answer': answer,
            'user_login': 'roca',
        }
    async with session.post('http://ogevtg.ru/api/check_task',headers=headers, json=json_answer_data, ssl=False) as res_answer:
        res_json = await res_answer.json()

        try:
            
            if res_json['status'] == 'wrong':
                print('Not solved', task_id)
                not_solved+=1
            elif res_json['status'] == "correct":
                print(
                    'Solved', task_id
                )
            else:
                print('Not solved, idk')
                not_solved+=1
        except Exception as e:
            print('Not solved:', e)
            print(res_json)
            not_solved+=1


async def solve(session):
    not_solved = 0
    for subject in subjects:
        json_data = {
            'subject': subject['name'],
            'types': subject['types'],
            'mode': 'all',
            'user_login': 'roca',
        }
        async with session.post('http://ogevtg.ru/api/get_tasks',headers=headers, json=json_data, ssl=False) as response:
            tasks = await response.json()
            tasks = tasks['tasks']
            async_tasks = []
            for task in tasks:
                async_tasks.append(
                    asyncio.create_task(
                        solve_task(not_solved, session, task, subject)
                    )
                )

            await asyncio.gather(*async_tasks)
    print('Did not solve', not_solved)

async def main():
    async with aiohttp.ClientSession() as session:
        await solve(session)

if __name__ == '__main__':
    asyncio.run(main())
            
                
