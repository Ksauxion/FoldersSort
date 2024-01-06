# FolderSort
A script which sorts all files in current directories and subdirectories in folders with its extensions.
## How to use
----------------------
```python FoldersSort.py [-h] [-r] [-o] [-e EXCEPTIONS]```

```-h``` or ```--help``` - shows help. <br >
```-r``` or ```--rename``` - Renames files with same names. Default is ```False```. <br >
```-o``` or ```--overwrite``` - Overwrites files with same names. Default is ```False```. <br >
```-e``` or ```--exceptions``` - Path to a file containing list of files which will not be organized, each on new line. Default is ```None```, but list contains script itself. <br >