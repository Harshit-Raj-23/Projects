import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL   
    )               
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, New_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, New_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()


def main():
    while True:
        print("\n Youtube Manager App ")
        print("Choose an Option : ")
        print("1. List all videos.")
        print("2. Add video.")
        print("3. Update a video.")
        print("4. Delete a video.")
        print("5. Exit app.")
        
        choice = input("Enter your choice : ")
        
        if choice == '1':
            list_all_videos()
            
        elif choice == '2':
            name = input("Enter video name : ")
            time = input("Enter video time : ")
            add_video(name, time)
            
        elif choice == '3':
            video_id = int(input("Enter video ID to be updated : "))
            name = input("Enter video name : ")
            time = input("Enter video time : ")
            update_video(video_id, name, time)
            
        elif choice == '4':
            video_id = int(input("Enter video ID to be deleted : "))
            delete_video(video_id)
            
        elif choice == '5':
            break
        
        else:
            print("Invalid choice.")
  
    conn.close()
    
if __name__ == "__main__":
    main()          