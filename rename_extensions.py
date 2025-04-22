import os
import sys

def rename_extensions(directory, old_ext, new_ext):
    """
    批量修改指定目录下的文件后缀
    :param directory: 要处理的目录路径
    :param old_ext: 原始后缀（如 '.txt'）
    :param new_ext: 新后缀（如 '.doc'）
    """
    # 确保后缀名格式正确（带点）
    if not old_ext.startswith('.'):
        old_ext = '.' + old_ext
    if not new_ext.startswith('.'):
        new_ext = '.' + new_ext

    # 统计计数器
    count = 0
    
    try:
        # 遍历指定目录
        for filename in os.listdir(directory):
            # 检查文件是否具有指定的后缀
            if filename.endswith(old_ext):
                # 构建新的文件名
                new_filename = filename[:-len(old_ext)] + new_ext
                # 构建完整的文件路径
                old_file = os.path.join(directory, filename)
                new_file = os.path.join(directory, new_filename)
                
                try:
                    # 重命名文件
                    os.rename(old_file, new_file)
                    count += 1
                    print(f"已重命名: {filename} -> {new_filename}")
                except OSError as e:
                    print(f"重命名 {filename} 失败: {e}")
        
        print(f"\n完成! 共重命名了 {count} 个文件。")
    
    except Exception as e:
        print(f"发生错误: {e}")

def main():
    # 检查命令行参数
    if len(sys.argv) != 4:
        print("使用方法:")
        print("python rename_extensions.py <目录路径> <原后缀> <新后缀>")
        print("示例: python rename_extensions.py C:\\Files txt doc")
        return

    # 获取命令行参数
    directory = sys.argv[1]
    old_ext = sys.argv[2]
    new_ext = sys.argv[3]

    # 检查目录是否存在
    if not os.path.exists(directory):
        print(f"错误: 目录 '{directory}' 不存在!")
        return

    # 执行重命名操作
    rename_extensions(directory, old_ext, new_ext)

if __name__ == "__main__":
    main() 