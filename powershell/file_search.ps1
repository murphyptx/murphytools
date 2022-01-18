# Set your search directory and destination directory
# $destdir = "[destination for files]"
$searchdir = "D:\"

# Create empty file to contain the full path info for each file
# echo $null > fullfilenames.txt -- this works at CLI, but may not work as part of a script, use the following instead:
Out-File -FilePath fullfilenames.txt # obvs, have this next to this ps1 file

# Populate array with file names
$filenames = Get-Content filenames.txt

# For each file in the filenames array, get the full path and assign to var $fullname
$allthefiles = ForEach ($file in $filenames) {$fullname = Get-ChildItem $searchdir | ? {$_.Name -ne "Windows" } | % {Get-ChildItem $_.FullName -filter $file -Recurse} | ForEach-Object {$_.FullName}}

$allthefiles | ForEach-Object {Out-File -FilePath fullfilenames.txt -Append}

# (foreach ($file in $filenames) {$fullname = Get-ChildItem $searchdir | ? {$_.Name -ne "Windows" } | % {Get-ChildItem $_.FullName -filter $file -Recurse} | ForEach-Object {$_.FullName}) | Out-File
