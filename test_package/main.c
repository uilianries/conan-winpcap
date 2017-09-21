/**
 * \file
 * \brief List network card and collect information
 *
 * Copyright 2017 Uilian Ries <uilianries@gmail.com>
 */
#include <assert.h>
#include <stdlib.h>
#include <pcap.h>

int main(int argc, char **argv)
{
    char errbuf[PCAP_ERRBUF_SIZE] = {0};
    bpf_u_int32 netp = 0;
    bpf_u_int32 maskp = 0;
    const char* dev = NULL;

    dev = pcap_lookupdev(errbuf);
    if (dev != NULL) {
        if (pcap_lookupnet(dev, &netp, &maskp, errbuf) == -1) {
            fprintf(stderr, "Couldn't get netmask for device %s: %s\n", dev, errbuf);
        }
    }

    return EXIT_SUCCESS;
}
