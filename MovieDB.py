import requests
import csv
import time

r1=[]
r1_id=[]
r2=[]

with open('movie_ID_name.csv', 'w', newline='') as csvfile1:
    fieldnames_1 = ['movie-ID', 'movie-name']
    writer1 = csv.DictWriter(csvfile1, fieldnames=fieldnames_1)

    for p in range(1, 16):
        time.sleep(0.25)
        r1.append(requests.get('https://api.themoviedb.org/3/discover/movie?api_key=a8921e0f501bcc43a65ce700f5d851ec&with_genres=35&sort_by=popularity.desc&primary_release_date.gte=2000-01-01&page=' + str(p)).json())
        for j in r1[p-1]['results']:
            writer1.writerow({'movie-ID': j['id'], 'movie-name': j['title']})
            r1_id.append(j['id'])

with open('movie_ID_sim_movie_ID.csv', 'w', newline='') as csvfile2:
    fieldnames_2 = ['movie-ID','similar-movie-ID']
    writer2 = csv.DictWriter(csvfile2, fieldnames=fieldnames_2)

    print(r1_id)

    for i in r1_id:
        r2.append(requests.get('https://api.themoviedb.org/3/movie/' + str(i) + '/similar?api_key=a8921e0f501bcc43a65ce700f5d851ec&language=en-US&sort_by=popularity.desc').json())

    for j in range(300):
        print(r2[j])
        for k in r2[j]['results'][:5]:
            writer2.writerow({'movie-ID': r1_id[j], 'similar-movie-ID': k['id']})