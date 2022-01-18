 Get-ChildItem D:\ | ? {$_.Name -ne "Windows" } | % {Get-ChildItem $_.FullName -filter 'windsong.pdf' -Recurse}
