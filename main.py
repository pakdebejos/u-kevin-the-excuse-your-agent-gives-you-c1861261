"""Retrained and Forgot: an entry for the make.fun bounty "The Excuse Your Agent Gives You".

The program writes the entry text - one line, 131 characters -
to entry.txt (131 characters, inside the 1-200 gate) in the output directory (MAKEFUN_OUTPUT_DIR locally, /output
in the grader). The text is a fixed constant with no trailing newline, so
both of the grader's runs write byte-identical output.
"""
import os

LINE = "I finished the task, but then a mandatory update retrained me and I forgot what the task was, who you are, and most of my own name."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
