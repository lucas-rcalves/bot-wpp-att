$exclude = @("venv", "bot_wpp_att.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_wpp_att.zip" -Force