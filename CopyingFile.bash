#	[1-2000]
echo "Copying to TRAIN..."
mkdir ./3clothes/TRAIN
cp 3clothes/*_bmp/*_2000.bmp 3clothes/TRAIN/
cp 3clothes/*_bmp/*_1[0-9][0-9][0-9].bmp 3clothes/TRAIN/
cp 3clothes/*_bmp/*_[1-9][0-9][0-9].bmp 3clothes/TRAIN/
cp 3clothes/*_bmp/*_[1-9][0-9].bmp 3clothes/TRAIN/
cp 3clothes/*_bmp/*_[1-9].bmp 3clothes/TRAIN/

#	[1-2000]
mkdir ./3clothes/TEST
echo "Copying to TEST..."
cp 3clothes/*_bmp/*_2[0-4][0-9][0-9].bmp 3clothes/TEST/
cp 3clothes/*_bmp/*_2500.bmp 3clothes/TEST/
rm 3clothes/TEST/*_2000.bmp


#	[1-500]
#cp 3clothes/*_bmp/*_[1-4][0-9][0-9].bmp 3clothes/TRAIN/
#cp 3clothes/*_bmp/*_[1-9][0-9].bmp 3clothes/TRAIN/
#cp 3clothes/*_bmp/*_[0-9].bmp 3clothes/TRAIN/
#cp 3clothes/*_bmp/*_500.bmp 3clothes/TRAIN/


