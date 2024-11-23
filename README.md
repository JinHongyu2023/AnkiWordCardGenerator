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
