class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2  # Sol yarıda kaç eleman olmalı
        
        # Binary Search'ü her zaman kısa olan dizi üzerinde yapalım
        # Bu sayede karmaşıklık O(log(min(m, n))) olur
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A)
        
        while l <= r:
            i = (l + r) // 2      # A dizisindeki kesme noktası
            j = half - i          # B dizisindeki kesme noktası (kalan elemanlar)
            
            # A'nın sol ve sağ parçalarının sınır değerleri (Edge case: sonsuzluk)
            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < len(A) else float("inf")
            
            # B'nin sol ve sağ parçalarının sınır değerleri
            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < len(B) else float("inf")
            
            # Bölme işleminin doğru olup olmadığını kontrol et
            if A_left <= B_right and B_left <= A_right:
                # DOĞRU BÖLME BULUNDU
                
                # Toplam eleman sayısı tek ise: Sol taraftaki en büyük sayı medyan
                if total % 2:
                    return max(A_left, B_left)
                
                # Toplam eleman sayısı çift ise: Ortadaki iki sayının ortalaması
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            elif A_left > B_right:
                # A'nın sol tarafı çok büyük, kesme noktasını sola kaydır
                r = i - 1
            else:
                # A'nın sol tarafı çok küçük, kesme noktasını sağa kaydır
                l = i + 1