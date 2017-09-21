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
    pcap_if_t *alldevs = NULL;
    pcap_if_t *it = NULL;
    const char* dev = NULL;

    dev = pcap_lookupdev(errbuf);
    if (dev != NULL) {
        if (pcap_lookupnet(dev, &netp, &maskp, errbuf) == -1) {
            fprintf(stderr, "Couldn't get netmask for device %s: %s\n", dev, errbuf);
        }
    }

    if (pcap_findalldevs(&alldevs, errbuf) == -1) {
        fprintf(stderr,"Couldn't execute pcap_findalldevs: %s\n", errbuf);
	return EXIT_SUCCESS;
    }

    for (it = alldevs; it != NULL; it = it->next) {
        printf("NAME: %s\n", it->name);
        if (it->description) {
            printf("DESCRIPTION: %s\n", it->description);
        }
        printf("IS LOOPBACK: %s\n\n", (it->flags & PCAP_IF_LOOPBACK) ? "YES":"NO");
    }

    pcap_freealldevs(alldevs);

    return EXIT_SUCCESS;
}
