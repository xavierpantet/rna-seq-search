# RNA Sequence Search

A lightweight, flexible pipeline for searching RNA sequences (including reverse complements) in genomic datasets using fuzzy matching. Supports common formats like BAM, SAM, CRAM, and FASTQ.

---

## 📦 Dependencies

- [`samtools`](http://www.htslib.org/) - for header extraction and format conversion
- [`seqkit`](https://bioinf.shenwei.me/seqkit/) - for fast and fuzzy sequence matching in FASTQ files
- Python ≥ 3.6

---

## 🔧 Features

- ✅ Supports BAM, SAM, CRAM, and FASTQ file formats
- ✅ Fuzzy search across sequences, allowing mismatches and multi-line matches
- ✅ Option to search reverse complements

---

## 🚀 Usage Pipeline

1. Create a folder under `data/` to store your dataset.
2. Download the dataset using [PyEGA3](https://github.com/EGA-archive/ega-download-client), with `--output-dir` pointing to your new folder.
3. Convert `.bam`, `.sam`, or `.cram` files into `.fastq` using:
   ```bash
   samtools fastq your_file.bam > your_file.fastq
   ```
4. Create a `sequences.txt` file:
   - Line 1: common sequence
   - Lines 2+: specific subsequences
5. Run the main script:
   ```bash
   python3 main.py --dataset my_dataset --sequence-file sequences.txt --with-reverse-complement
   ```

Results will be saved to:
- `data/[DATASET]/matches/common/common_matches.fastq`
- `data/[DATASET]/matches/specific/[SEQUENCE]_matches.fastq`

---

## 🪄 Useful Commands

```bash
# View header of a BAM/SAM/CRAM file
samtools view -H your_file.bam > your_file.header.bam

# Convert BAM/SAM/CRAM to FASTQ
samtools fastq your_file.cram > your_file.fastq
```

---

## 💡 Command-Line Arguments

```bash
python3 main.py --dataset [DATASET] --sequence-file [SEQUENCE_FILE] [--with-reverse-complement]
```

| Parameter              | Type     | Description                                                                 |
|------------------------|----------|-----------------------------------------------------------------------------|
| `--dataset`            | string   | Name of the dataset folder in `data/`.                                     |
| `--sequence-file`      | string   | Path to the sequence list file (first line is common, others are specific) |
| `--with-reverse-complement` | flag     | If included, searches reverse complements as well.                         |
