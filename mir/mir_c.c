#include "mir_c.h"

double isotonic_regression(double const* const inp, double const* const out, unsigned n, int direction) {
    unsigned j, k, i;
    char pooled;
    double const* pinp;
    double* pout;
    double err = 0;
    if (n > 1) {
        pinp = inp;
        pout = out;
        for (i = 0; i < n; i++)
            *pout++ = *pinp++ * direction;
        n -= 1;
        while (1) {
            pooled = i = 0;
            while (i < n) {
                k = i;
                while ((k < n) & (out[k] >= out[k + 1]))
                    k++;
                pout = &out[i];
                if (*pout != out[k]) {
                    double acc = 0.0;
                    for(j = i; j < k + 1; j++)
                        acc += *pout++;
                    acc /= k - i + 1;
                    for(j = i; j < k + 1; j++)
                        *--pout = acc;
                    pooled = 1;
                }
                i = k + 1;
            }
            if (!pooled)
                break;
        }
    }
    pinp = inp;
    pout = out;
    for (i = 0; i < n; i++) {
        *pout *= direction;
        err += (*pinp - *pout) * (*pinp++ - *pout++);
    }
    return err;
}
