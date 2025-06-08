for folder in h1 haf41 hafta11 hafta11-extra hafta13 hafta15; do
  git log --pretty=format:"%h - %an - %ad : %s" --date=short -- "$folder" > "$folder/log.txt"
done
