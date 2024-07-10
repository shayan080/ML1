
src="D:\myfile - Copy"
destination="D:\otherfile - Copy"


mkdir -p "$destination/images"
mkdir -p "$destination/txt"
mkdir -p "$destination/json"


mv "$src"/*.{jpg,jpeg,png} "$destination/images"


mv "$src"/*.txt "$destination/txt"

mv "$src"/*.json "$destination/json"

echo "Files moved successfully!"
