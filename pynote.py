#!/usr/bin/python
#!/bin/python
#!/sbin/python
import json
import os
import sys
from datetime import datetime

DB_FILE = "note.json"

# Function to load notes from the JSON file
def load_notes():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

# Function to save notes to the JSON file
def save_notes(notes):
    with open(DB_FILE, "w") as f:
        json.dump(notes, f, indent=4)

# Function to add a new note
def add_note():
    description = input("Enter the description: ")
    note = input("Enter your note:\n\n ")
    current_datetime = datetime.now().strftime("%Y.%b.%d , %I:%M%p")
    new_note = {
        "date": current_datetime,
        "description": description,
        "note": note
    }
    notes = load_notes()
    notes.append(new_note)
    save_notes(notes)
    print("Note saved successfully!")

# Function to view all notes
def view_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
    else:
        for i, note in enumerate(notes, start=1):
            print(f"[{note['date']}]")
            print(f"ID: {i}")
            print(f"Description: {note['description']}")
            print(f"Note: {note['note']}")
            print()

# Function to delete a note by ID
def delete_note():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return

    note_id = input("Enter the ID of the note to delete: ")
    if note_id.isdigit() and 1 <= int(note_id) <= len(notes):
        notes.pop(int(note_id) - 1)
        save_notes(notes)
        print("Note deleted successfully.")
    else:
        print("Invalid note ID.")

# Function to delete all notes
def delete_all_notes():
    confirmation = input("Are you sure you want to delete all notes? (y/n): ")
    if confirmation.lower() == "y":
        os.remove(DB_FILE)
        print("All notes deleted successfully.")
    else:
        print("Deletion canceled.")

# Function to search notes by description or note content
def search_notes():
    search_query = input("Enter the search query: ")
    notes = load_notes()
    matching_notes = []
    for note in notes:
        if search_query.lower() in note["description"].lower() or search_query.lower() in note["note"].lower():
            matching_notes.append(note)
    if not matching_notes:
        print("No matching notes found.")
    else:
        for i, note in enumerate(matching_notes, start=1):
            print(f"[{note['date']}]")
            print(f"ID: {i}")
            print(f"Description: {note['description']}")
            print(f"Note: {note['note']}")
            print()

# Function to clear the terminal screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Function to display the help menu
def display_help():
    print("Usage: pynote.py [options]")
    print("Options:")
    print("  -a     Add a new note")
    print("  -v     View all notes")
    print("  -d     Delete a note by ID")
    print("  -da    Delete all notes")
    print("  -s     Search for notes")
    print("  -h     Display this help menu")

# Main function to handle user actions
def main():
    if len(sys.argv) < 2:
        display_help()
        return

    action = sys.argv[1]
    if action == "-a":
        clear_screen()
        add_note()
    elif action == "-v":
        clear_screen()
        view_notes()
    elif action == "-d":
        clear_screen()
        delete_note()
    elif action == "-da":
        clear_screen()
        delete_all_notes()
    elif action == "-s":
        clear_screen()
        search_notes()
    elif action == "-h":
        display_help()
    else:
        print("Invalid action.")

if __name__ == "__main__":
    main()

