import streamlit as st
import json

# Load & save libary data

def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []    
    
def save_library():
    with open("Library.json" ,"w") as file:
        json.dump(library, file, indent=4)

# initilize library
library = load_library()

st.title("Library Management System 🗒")
menu = st.sidebar.radio("Select an option", ["View Library", "Add Book", "Remove Book","Search Book", "Save and Exit"])

if menu == "View Library":
    st.sidebar.write("Your Library")
    if library:
        st.table(library)
    else:
        st.write("No books in the library. Add some books!")

# Add books
elif menu == "Add Book":

    st.sidebar.write("Add a new Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("year", min_value=2022, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read_status = st.selectbox("Read Status", ["Read", "Unread"])



    if st.button("Add Book"):
        library.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status})
        save_library()
        st.success("BOOKS added to the library!")
        st.rerun()


# Remove books 
elif menu == "Remove Book":
    st.sidebar.write("Remove a book")
    book_titles = [book["title"] for book in library]

    if book_titles:
        selected_book = st.selectbox("Select a book to remove", book_titles)
        if st.button("Remove Book"):
            library = [book for book in library if book["title"] != selected_book]
            save_library()
            st.success("Book removed from the library!")
            st.rerun()
    else:
        st.warning("No books in the library to remove. Add some books first!")


# Search books
# elif menu == "Search Book":
#     st.sidebar("Search a book")
#     search_term = st.text_input("Enter a title orauthor name")
    
#     if st.button("Search"):
#       results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
#     if results:
#         st.table(results)
#     else:
#         st.warning("No books found!.")
# Search books
elif menu == "Search Book":
    st.sidebar.write("Search a book")
    search_term = st.text_input("Enter a title or author name")
    
    results = []
    if st.button("Search"):
        results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("No books found!")


#save and exit
elif menu == "Save and Exit":
    save_library()
    st.success("Library saved successfully!")
   













    
