FROM busybox:1.36-uclibc as busybox

FROM bkimminich/juice-shop

COPY --from=busybox /bin/sh /bin/sh
COPY --from=busybox /bin/wget /bin/wget

HEALTHCHECK --interval=5s --start-period=30s \
  CMD /bin/wget --tries=1 --spider http://localhost:3000 || exit 1
