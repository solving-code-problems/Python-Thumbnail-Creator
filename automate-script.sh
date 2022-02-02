if [ "$#" -ne 2 ]; then
  echo "Expecting 2 arguments"
  echo "Example usage ./automate-script <heading> <subheading>"
  exit 1
fi

python3 main.py --text $1 --pos 20,20 --size 150 --input default.png --out temp.png
python3 main.py --text $2 --pos 20,220 --size 75 --input temp.png --out result2.png
rm temp.png
