text2 = """Python is a powerful programming language. It's easy to learn and versatile!
        You can use Python for web development, data science, and automation. The syntax is clean and readable.
        This makes Python perfect for beginners and expers alike."""

print(f"Characters: {len(text2)}")
print(f"Words: {len(text2.split())}")
print(f"Sentences: {(text2.count('.') + text2.count('!') + text2.count('?'))}")