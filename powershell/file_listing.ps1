# returns file listing
# does NOT include empty directories or directories without files at their root
#
gci -r -Attributes !Directory | Select-Object Directory, Name, @{Name="KB";Expression={"{0:f0}" -f ($_.Length / 1KB) }}, @{Name="MB";Expression={"{0:f3}" -f ($_.Length / 1MB) }}, @{Name="GB";Expression={"{0:f3}" -f ($_.Length / 1GB) }} | Export-Csv <path_to_csv>.csv -NoTypeInformation
