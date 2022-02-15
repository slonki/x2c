#! /usr/bin/env python

#
#    x2c - XML to CSV Conversion
#    Copyright (C) 2022  Martin Valter
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import xml.etree.ElementTree as et
import pandas as pd
import sys, argparse

def convert():
    args = sys.argv[1:]

    inputfile = ''
    outputfile = ''
    cols = []
    rows = []

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--outfile')
    parser.add_argument('-i', '--infile') 
    args = parser.parse_args()

    outfile = args.outfile
    infile = args.infile

    xmlparse = et.parse(infile)
    root = xmlparse.getroot()

    for element in root:
        tmp_d = {}

        t_atts = element.attrib
            for a in t_atts:
                tmp_d[a] = t_atts[a]
                cols.append(a)

        for l in element:
            atts = l.attrib
            for a in atts:
                tmp_d[a] = atts[a]
                cols.append(a)

        tmp_d[l.tag] = l.text
        cols.append(l.tag)
    
        rows.append(tmp_d)
    
    cols = list(set(cols)
    
    f = pd.DataFrame(rows, columns=cols)    
    f.to_csv(outfile)