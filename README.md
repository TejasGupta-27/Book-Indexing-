# Lexicon - Red-Black Tree for Word Indexing

Lexicon is a Python project that implements a Red-Black Tree for efficient word indexing within a set of chapters. This project includes classes for a Red-Black Tree (`RedBlackTree`), a Lexicon for indexing words (`Lexicon`), and a Most Recently Used cache (`MRU`).

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The project consists of three main components:

1. **Red-Black Tree (`RedBlackTree`):**
   - Implements a self-balancing binary search tree for efficient word storage.
   - Supports insertion, deletion, and searching operations.

2. **Lexicon (`Lexicon`):**
   - Utilizes the Red-Black Tree to index words within a set of chapters.
   - Handles word processing, chapter reading, and common word pruning.
   - Builds an index and provides functionalities for accessing word occurrences.

3. **Most Recently Used Cache (`MRU`):**
   - Manages a cache of recently accessed index entries.
   - Supports access tracking and retrieval of the most recently used entry.

## Features

- Efficient Red-Black Tree implementation.
- Word indexing within chapters using a Lexicon.
- Common word pruning to enhance indexing efficiency.
- MRU cache for tracking recently accessed index entries.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/lexicon.git
    cd lexicon
    ```

2. Run the example script or integrate the Lexicon class into your project:

    ```bash
    python example.py
    ```

## Usage

1. Create a `Lexicon` instance:

    ```python
    lex = Lexicon()
    ```

2. Read chapters and build the index:

    ```python
    chapter_names = ["chapter1.txt", "chapter2.txt", ...]
    lex.read_chapters(chapter_names)
    ```

3. Access word occurrences and most recently used entries:

    ```python
    index = lex.build_index()
    mru_cache = MRU(max_size=10)
    entry = lex.search("example")
    mru_cache.access(entry)
    most_recent_entry = mru_cache.get_most_recent()
    ```

