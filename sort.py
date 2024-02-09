from itertools import groupby
import argparse
import json
import os
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=argparse.FileType('r'), default=sys.stdin, help='The input ndjson from the USPS collection box spider')
    parser.add_argument('output', type=argparse.FileType('w'), default=sys.stdout, help='The output ndjson to write the sorted data to')
    parser.add_argument('--prefix-dir', help='Specify this to also write data into files by prefix of the ID for each collection box. The value is the directory to write to.')
    parser.add_argument('--prefix-chars', type=int, default=2, help='The number of characters of the collection box ID to use as prefix')
    args = parser.parse_args()

    features = []
    for line in args.input:
        features.append(json.loads(line))

    for feature in sorted(features, key=lambda f: f['properties']['ref']):
        args.output.write(json.dumps(feature, sort_keys=True) + '\n')

    if args.prefix_chars and args.prefix_dir:
        for k, features in groupby(sorted(features, key=lambda f: f['properties']['ref']), key=lambda i: i['properties']['ref'][:args.prefix_chars]):
            with open(os.path.join(args.prefix_dir, '%s.ndjson' % k), 'w') as f:
                for feature in features:
                    # Remove the scraped timestamp that was added in https://github.com/alltheplaces/alltheplaces/pull/5661
                    feature["properties"].pop("spider:collection_time", None)
                    feature.pop("dataset_attributes", None)

                    f.write(json.dumps(feature, sort_keys=True) + '\n')
