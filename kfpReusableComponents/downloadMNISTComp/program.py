import argparse
import gzip, wget
import struct, os
import numpy as np


def downloadFile(website):

    try:
        wget.download(website)
        if not os.path.exists('./data'):
            os.makedirs('data')

        folder, fileName = os.path.split(website)
        newFile = os.path.join('data', fileName)
        os.rename(fileName, newFile )

        return newFile

    except Exception as e:
        print(f'Unable to download file [{website}]: {e}')
        return None

    return

def readImages(fileName):

    try:
        with open(fileName, 'rb') as f:
            temp = f.read(4*4)
            magicNumber, N, rows, cols = struct.unpack('>llll', temp)
            print(magicNumber, N, rows, cols)

            nPixels = N*rows*cols

            formatString = f'>{nPixels}B'
            nBytes = f.read( nPixels )

            data = struct.unpack(formatString, nBytes)
            data = np.array( data )
            data = data.reshape((N, -1))
            print(data.shape)


    except Exception as e:
        print(f'Problem: {e}')

    return

def createParser():

    parser = argparse.ArgumentParser(description='Download MNIST data')
    
    # Figure out what action should be taken
    parser.add_argument('--download', dest='todo', action='store_const', const='download', help='download the requested file')
    parser.add_argument('--extract',  dest='todo', action='store_const', const='extract',  help='unzip the .gz files into the same folder')
    parser.add_argument('--toNumpy',  dest='todo', action='store_const', const='toNumpy',  help='convert unzipped files to numpy files')
    
    # specifications of what should be downloaded
    parser.add_argument('--url', type=str, help='download data at the specifid url')
    
    parser.add_argument('--output-path', type=str, help='Path of the local file where the Output 1 data should be written.') # Paths should be passed in, not hardcoded
    
    args = parser.parse_args()

    if args.todo =='download' and args.url is None:
        print(f'when you use the [--download] argument you will also need to provide the [--url] argument.')
        pring(f'python3 --download --url "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"')


    return args

def main():

    args = createParser()
    print(args)

    if (args.todo == 'download') and (args.url is not None):
        result = downloadFile(args.url)
        print(result)
        if args.output_path is not None:
            with open( args.output_path, 'w' ) as fOut:
                fOut.write( f'{result}' )

    # if True:
    #     readImages('data/train-images-idx3-ubyte')

    # if False:
    #     downloadFile(website)
        
    # if False:
    #     with gzip.open('data/train-images-idx3-ubyte.gz', 'rb') as fIn: 
    #         with open('data/train-images-idx3-ubyte', 'wb') as fOut: 
    #             fOut.write( fIn.read()  ) 

    return

if __name__ == "__main__":
    main()
