# VirtualLibrary

# What
3D app where a user can walk around a library, pick books off shelves, and read

# How
- Mainly in Unreal Engine 4
- Uses Project Gutenberg (mirrors) to grab public domain books as text files
- Some python scripts for getting metadata (category of books for sorting) and checking for updates/new books

# Why
Not entirely sure yet

# To Do
- generate internal database - ID and categories (possibly title, author, and sort as well) - via metadata from https://www.gutenberg.org/cache/epub/feeds/ - this will be done via a python file run once on my pc
- use db to arrange books by category (exclude repeats)
- make a 3d library
- find 3d models for books, turning pages
- decide when to run web request code (walk into section, now we need all titles OR do I just store all of this and only do a web request for the book's text?)
- daily update script - on startup, check rss file at https://www.gutenberg.org/cache/epub/feeds/ for updates, add to internal db (haven't found an example where category is listed though)
