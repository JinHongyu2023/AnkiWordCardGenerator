import os
import shutil
from gtts import gTTS
from googletrans import Translator
from nltk.corpus import wordnet as wn
import eng_to_ipa
import tkinter as tk
from tkinter import filedialog, messagebox

# 初始化翻译工具
translator = Translator()

# 词性映射
WORDNET_TO_COMMON_POS = {
    'a': 'adj',  # 形容词
    'n': 'n',    # 名词
    'v': 'v',    # 动词
    'r': 'adv'   # 副词
}

# 主处理函数
def process_words(input_words, output_dir, media_dir, prefix):
    words = [word.strip() for word in input_words.replace("，", ",").split(",") if word.strip()]
    anki_data = []  # 保存每个单词的独立卡片

    for word in words:
        print(f"正在处理单词：{word}")  # 调试信息
        # Step 1: 为每个单词生成音频文件（带前缀命名）
        audio_file = generate_audio(word, output_dir, media_dir, prefix)

        # Step 2: 获取单词信息，包括词性、中文翻译和音标
        word_data = get_word_data(word)

        # Step 3: 组织 Anki 卡片格式
        anki_entry = create_anki_entry(word, audio_file, word_data)
        anki_data.append(anki_entry)

    # Step 4: 输出为 Anki 文件
    output_anki_file(anki_data, output_dir)
    messagebox.showinfo("完成", "Anki 文件和音频已成功生成！")

# 生成音频文件，并复制到 collection.media
def generate_audio(word, output_dir, media_dir, prefix):
    audio_filename = f"{prefix}_{word}.mp3"
    local_audio_path = os.path.join(output_dir, audio_filename)
    media_audio_path = os.path.join(media_dir, audio_filename)

    # 生成音频文件
    tts = gTTS(text=word, lang="en", tld="co.uk")
    tts.save(local_audio_path)
    print(f"生成音频文件：{local_audio_path}")  # 调试信息

    # 将音频文件复制到 collection.media
    shutil.copy(local_audio_path, media_audio_path)
    print(f"复制到媒体文件夹：{media_audio_path}")  # 调试信息

    return audio_filename

# 获取单词信息：词性、中文翻译和国际音标
def get_word_data(word):
    synsets = wn.synsets(word)
    if synsets:
        # 提取第一个 synset 的词性
        wordnet_pos = synsets[0].pos()
        # 映射到通用词性
        pos = WORDNET_TO_COMMON_POS.get(wordnet_pos, "未知")
    else:
        pos = "未知"

    # 翻译
    translation = translator.translate(word, src="en", dest="zh-cn").text

    # 获取国际音标（IPA）
    phonetics_raw = eng_to_ipa.convert(word)
    phonetics = f"/{phonetics_raw}/" if phonetics_raw else "/暂无音标/"

    return {
        "word": word,
        "pos": pos,
        "translation": translation,
        "phonetics": phonetics,
    }

# 创建独立的 Anki 卡片条目
def create_anki_entry(word, audio_file, word_data):
    # 卡片字段
    fields = [
        f"[sound:{audio_file}]",  # 正面播放音频
        word_data['word'],  # 单词拼写（答案部分）
        word_data['pos'],  # 词性
        word_data['translation'],  # 中文翻译
        word_data['phonetics'],  # 音标
    ]
    return " | ".join(fields)  # 使用竖线作为分隔符

# 输出为 Anki 导入文件
def output_anki_file(anki_data, output_dir, filename="anki_import.txt"):
    output_path = os.path.join(output_dir, filename)
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("\n".join(anki_data))
    print(f"Anki 文件已保存为：{output_path}")  # 调试信息

# 图形化界面
def gui():
    def generate():
        input_words = entry_words.get()
        if not input_words:
            messagebox.showwarning("警告", "请输入单词列表！")
            return
        if not output_dir.get():
            messagebox.showwarning("警告", "请选择输出目录！")
            return
        media_directory = media_dir.get() or "C:/Users/abh/AppData/Roaming/Anki2/账户 1/collection.media"
        prefix_value = prefix.get().strip()
        if not prefix_value:
            messagebox.showwarning("警告", "请输入音频文件前缀！")
            return
        process_words(input_words, output_dir.get(), media_directory, prefix_value)

    def select_output_directory():
        directory = filedialog.askdirectory()
        if directory:
            output_dir.set(directory)

    def select_media_directory():
        directory = filedialog.askdirectory()
        if directory:
            media_dir.set(directory)

    # 创建窗口
    root = tk.Tk()
    root.title("Anki 生成工具")

    # 单词列表输入
    tk.Label(root, text="请输入单词列表（中/英文逗号分隔）：").grid(row=0, column=0, padx=10, pady=5)
    entry_words = tk.Entry(root, width=50)
    entry_words.grid(row=0, column=1, padx=10, pady=5)

    # 前缀输入
    tk.Label(root, text="音频文件前缀：").grid(row=1, column=0, padx=10, pady=5)
    prefix = tk.StringVar()
    entry_prefix = tk.Entry(root, textvariable=prefix, width=50)
    entry_prefix.grid(row=1, column=1, padx=10, pady=5)

    # 输出目录选择
    tk.Label(root, text="输出目录（保存文件）：").grid(row=2, column=0, padx=10, pady=5)
    output_dir = tk.StringVar()
    entry_output = tk.Entry(root, textvariable=output_dir, width=50)
    entry_output.grid(row=2, column=1, padx=10, pady=5)
    tk.Button(root, text="选择", command=select_output_directory).grid(row=2, column=2, padx=10, pady=5)

    # 媒体目录选择
    tk.Label(root, text="媒体目录（collection.media）：").grid(row=3, column=0, padx=10, pady=5)
    media_dir = tk.StringVar()
    entry_media = tk.Entry(root, textvariable=media_dir, width=50)
    entry_media.grid(row=3, column=1, padx=10, pady=5)
    tk.Button(root, text="选择", command=select_media_directory).grid(row=3, column=2, padx=10, pady=5)

    # 生成按钮
    tk.Button(root, text="生成 Anki 文件", command=generate, bg="green", fg="white").grid(row=4, column=1, pady=10)

    root.mainloop()


if __name__ == "__main__":
    import nltk
    nltk.download("wordnet")  # 确保下载WordNet数据
    gui()
