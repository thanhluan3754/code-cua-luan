import time
import os
import winsound

def main():
    current_folder = os.path.dirname(os.path.abspath(__file__))
    filename = "music.wav"
    sound_file = os.path.join(current_folder, filename)

    if not os.path.exists(sound_file):
        print(f"Lỗi: Không tìm thấy file tại: {sound_file}")
        return
 
    end_icons = [
        "✨ ",
        "🎶 ",
        "🥀 ",
        "❤️ ",
        "💬 ",
        "🍂 ",
        "💔 ",
        "🌅 "
    ]

    lyrics_by_lines = [
        [
            (1.09, "Đêm 🌙"), (1.73, "mang"), (2.6, "em"), (3.07, "về"), (3.38, "trong"), (3.76, "giấc"), (4.19, "mơ")
        ],
        [
            (7.8, "Tôi"), (8.56, "hát 🎤"), (9.47, "lên"), (9.92, "trăm"), (10.22, "lời"), (10.64, "vu"), (11.11, "vơ")
        ],
        [
            (14.64, "Vẫn"), (15.38, "những"), (16.19, "khuôn"), (16.65, "mặt"), (17.05, "cười 🎭"), (17.76, "dù"), (17.97, "biết"), (18.43, "sẽ"), (18.71, "không"), (19.15, "hề"), (19.6, "vui")
        ],
        [
            (21.08, "Dù"), (21.32, "hôm"), (21.58, "nay"), (21.99, "dẫu"), (22.21, "đúng"), (22.59, "sai ⏳"), (23.26, "vẫn"), (23.68, "yêu"), (23.91, "hơn"), (24.39, "ngày"), (24.87, "mai")
        ],
        [
            (27.46, "Xin"), (27.8, "lỗi 😿"), (28.24, "người"), (28.77, "vì"), (29.08, "những"), (29.49, "điều"), (29.9, "chưa"), (30.37, "nói"), (30.73, "ra"), (31.17, "thành"), (31.65, "câu")
        ],
        [
            (34.31, "Xin"), (34.57, "lỗi 😿"), (35.05, "người"), (35.61, "vì"), (35.87, "bao"), (36.29, "ngày"), (36.76, "qua"), (37.28, "đã"), (37.57, "trôi"), (38.07, "về"), (38.54, "đâu")
        ],
        [
            (41.12, "Mất"), (41.4, "bao"), (41.91, "lâu ⏳"), (42.52, "để"), (42.77, "ta"), (43.17, "tạm"), (43.63, "quên"), (44.06, "u"), (44.5, "sầu"), (45.37, "để"), (45.57, "tim 💔"), (45.98, "này"), (46.24, "vơi"), (46.64, "cơn"), (47.1, "đau 💔")
        ],
        [
            (48.7, "Và"), (48.98, "những"), (49.38, "ký"), (49.67, "ức 🎞️"), (50.04, "mệt"), (50.51, "nhoài"), (51.07, "chợt"), (51.47, "tan"), (51.91, "vào"), (52.36, "sớm"), (52.82, "mai")
        ]
    ]

    try:
        winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
    except Exception as e:
        print("Lỗi phát nhạc:", e)
        return

    start_time = time.time()
    
    os.system('cls' if os.name == 'nt' else 'clear')

    for i, line in enumerate(lyrics_by_lines):
        print()

        for timestamp, word in line:
            while True:
                elapsed = time.time() - start_time
                if elapsed >= timestamp:
                    break
                time.sleep(0.01)
            
            print(word, end=" ", flush=True)
        
        final_icon = end_icons[i] if i < len(end_icons) else ""
        print(final_icon, end="", flush=True)

        if i < len(lyrics_by_lines) - 1:
            next_line = lyrics_by_lines[i + 1]
            first_word_next_line_time = next_line[0][0]
            
            while True:
                elapsed = time.time() - start_time
                if elapsed >= first_word_next_line_time - 0.5:
                    break
                time.sleep(0.1)
            
            os.system('cls' if os.name == 'nt' else 'clear')

    time.sleep(5)

if __name__ == "__main__":
    main()