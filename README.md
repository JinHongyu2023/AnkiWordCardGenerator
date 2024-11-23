## **Project Introduction (English)**

Anki Word Card Generator is a Python-based tool designed to help users quickly generate Anki import files and audio files, enabling efficient creation of flashcards.

This tool automatically generates IPA (International Phonetic Alphabet), Chinese translations, and part-of-speech tags for words. Audio files are saved directly to Anki's `collection.media` folder. The tool provides a user-friendly graphical interface with no coding required.

---

### **Features**
1. **Multilingual Input**:
   - Accepts word lists separated by Chinese or English commas.
2. **IPA Generation**:
   - Automatically generates IPA using the `eng_to_ipa` library.
3. **Part-of-Speech Detection**:
   - Accurately categorizes parts of speech (noun, adjective, verb, adverb) using NLTK.
4. **Chinese Translations**:
   - Integrated with Google Translate for automatic Chinese translations.
5. **Audio Generation**:
   - Uses gTTS to generate MP3 files with British English pronunciation, saved directly to Anki's `collection.media` folder.
6. **Output Format**:
   - Generates Anki-compatible `.txt` files with the following card details:
     - Front: Audio.
     - Back: Word spelling, part of speech, Chinese translation, and IPA.

---

### **Installation**
#### **Requirements**
- Python 3.7 or higher.

#### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AnkiWordCardGenerator.git
   cd AnkiWordCardGenerator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure NLTK database is downloaded:
   ```bash
   python -m nltk.downloader wordnet
   ```

---

### **Usage**
1. Run the program:
   ```bash
   python anki_word_card.py
   ```
2. In the GUI:
   - Enter a word list (separated by Chinese or English commas).
   - Provide a custom prefix for audio files (e.g., `J001`).
   - Select the output directory for generated files.
   - Specify the media folder (default: `C:/Users/<Username>/AppData/Roaming/Anki2/<Profile Name>/collection.media`).
   - Click "Generate Anki File."

3. Import the generated `.txt` file into Anki.

---

### **Sample Output**
Input word list:
```plaintext
big, small, girl, boy
```

Generated `anki_import.txt`:
```plaintext
[sound:J001_big.mp3] | big | adj | big | /bɪg/
[sound:J001_small.mp3] | small | adj | small | /smɔl/
[sound:J001_girl.mp3] | girl | n | girl | /gərl/
[sound:J001_boy.mp3] | boy | n | boy | /bɔɪ/
```

Media files:
- `J001_big.mp3`
- `J001_small.mp3`
- `J001_girl.mp3`
- `J001_boy.mp3`

---

### **Dependencies**
- [gTTS](https://pypi.org/project/gTTS/) - For generating audio files.
- [googletrans](https://pypi.org/project/googletrans/) - For Chinese translations.
- [nltk](https://www.nltk.org/) - For part-of-speech tagging.
- [eng_to_ipa](https://pypi.org/project/eng-to-ipa/) - For generating IPA (International Phonetic Alphabet).

---

### **License**
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.



# **Anki Word Card Generator v1.0**

## **项目简介（中文）**

Anki Word Card Generator 是一个基于 Python 的工具，用于快速生成 Anki 导入文件和音频文件，帮助用户高效创建记忆卡片。

该工具支持自动生成单词的国际音标（IPA）、中文翻译及词性，并将音频文件存入 Anki 的 `collection.media` 文件夹。用户可通过简单的图形化界面完成操作，无需任何编程基础。

---

### **功能特点**
1. **多语言支持**：
   - 输入支持中文逗号或英文逗号分隔的单词列表。
2. **自动生成国际音标**：
   - 使用 `eng_to_ipa` 库生成标准国际音标（IPA）。
3. **词性识别**：
   - 通过 NLTK 提供准确的词性分类（名词、形容词、动词、副词）。
4. **中文翻译**：
   - 集成 Google Translate，自动生成单词中文释义。
5. **音频生成**：
   - 使用 gTTS 生成英式发音 MP3 文件，并自动存入 Anki 的 `collection.media` 文件夹。
6. **输出格式**：
   - 生成符合 Anki 导入标准的 `.txt` 文件，每张卡片包含：
     - 正面：音频。
     - 背面：单词拼写、词性、中文释义、国际音标。

---

### **安装说明**
#### **系统要求**
- Python 3.7 或更高版本。

#### **安装步骤**
1. 克隆项目到本地：
   ```bash
   git clone https://github.com/yourusername/AnkiWordCardGenerator.git
   cd AnkiWordCardGenerator
   ```
2. 安装依赖库：
   ```bash
   pip install -r requirements.txt
   ```
3. 确保下载 NLTK 数据库：
   ```bash
   python -m nltk.downloader wordnet
   ```

---

### **使用指南**
1. 运行程序：
   ```bash
   python anki_word_card.py
   ```
2. 在弹出的图形化界面中：
   - 输入单词列表（支持中/英文逗号分隔）。
   - 输入音频文件的自定义前缀（如 `J001`）。
   - 选择保存生成文件的输出目录。
   - 指定媒体文件目录（默认为 `C:/Users/<用户名>/AppData/Roaming/Anki2/<账户名>/collection.media`）。
   - 点击「生成 Anki 文件」。

3. 在 Anki 中导入生成的 `.txt` 文件即可。

---

### **输出示例**
输入单词列表：
```plaintext
big, small, girl, boy
```

生成的 `anki_import.txt` 文件内容：
```plaintext
[sound:J001_big.mp3] | big | adj | 大的 | /bɪg/
[sound:J001_small.mp3] | small | adj | 小的 | /smɔl/
[sound:J001_girl.mp3] | girl | n | 女孩 | /gərl/
[sound:J001_boy.mp3] | boy | n | 男孩 | /bɔɪ/
```

生成的媒体文件：
- `J001_big.mp3`
- `J001_small.mp3`
- `J001_girl.mp3`
- `J001_boy.mp3`

---

### **依赖列表**
- [gTTS](https://pypi.org/project/gTTS/)：生成音频文件。
- [googletrans](https://pypi.org/project/googletrans/)：获取中文翻译。
- [nltk](https://www.nltk.org/)：词性提取。
- [eng_to_ipa](https://pypi.org/project/eng-to-ipa/)：生成国际音标（IPA）。

---

### **许可证**
本项目遵循 MIT 开源许可证。详情请参阅 [LICENSE](./LICENSE)。

---


