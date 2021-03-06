# barcodeErrorProducer

Simple python script that takes a list of barcodes (strings) and creates an exhaustive list of versions of this barcode with a 1-bp change in each version (comma-separated).

I made this to prepare a list of the valid 10x barcodes that can be error-corrected in UMI-tools.

## Example

Assuming that the input barcode is the following `ATA`, the script will output this:

```
ATA CTA,GTA,TTA,AAA,ACA,AGA,ATC,ATG,ATT
```

The first column contains the input barcode and the second column contains the comma-separated mutated versions (1 bp at a time).

The number of mutated versions is equal to 3 times the length of the barcode (because each position can be changed to the three remaining nucleotides).

## Notes

I did not pay any attention to efficiency and speed since this usually needs to be run only once to create the list of interest. I parsed a list of ~737,000 barcodes of 16 bp each and it took 5-10 minutes on a regular machine.
