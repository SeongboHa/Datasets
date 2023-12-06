import os
import shutil
import argparse


def copy_color_and_depth(original_path, output_path):
    # Read all images files(depth, colors)
    images_path = os.path.join(original_path, "results")
    all_images = os.listdir(images_path)
    
    check = 0
    images = len(all_images)//2
    for file in all_images:
        if file[-3:] == "jpg":
            shutil.copy(os.path.join(images_path, file), f"{output_path}/images/{file}")
            check += 1
        elif file[-3:] == "png":
            shutil.copy(os.path.join(images_path, file), f"{output_path}/depth_images/{file}")
            check += 1
        print(f"processing... {check//2}/{images}")
    print(f"image copy check : {check//2}")


if __name__=="__main__":
    parser = argparse.ArgumentParser(
        description='Arguments to evaluate the reconstruction.'
    )
    parser.add_argument('--original', type=str,
                        help='original dataset path')
    parser.add_argument('--output', type=str,
                        help='output dataset path')
    args = parser.parse_args()
    
    original_dataset_path = args.original
    output_path = args.output
    
    # make dirs
    os.makedirs(os.path.join(output_path, "depth_images"), exist_ok=True)
    os.makedirs(os.path.join(output_path, "images"), exist_ok=True)
    
    # copy image files(depth, color)
    copy_color_and_depth(original_dataset_path, output_path)
    
    # copy traj file
    shutil.copy(os.path.join(original_dataset_path, "traj.txt"), \
                os.path.join(output_path, "traj.txt"))