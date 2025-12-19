import { defineCollection, z } from 'astro:content';

const activitiesCollection = defineCollection({
    type: 'content',
    schema: z.object({
        year: z.number(),
        summary: z.string(),
        // galleryImages: 画像ファイル名の配列（パスのprefixはコンポーネント側で付与想定）
        galleryImages: z.array(z.string()).optional(),
    }),
});

const profileCollection = defineCollection({
    type: 'content',
    schema: z.object({
        name: z.string(),
        title: z.string(),
        image: z.string(),
        tags: z.array(z.string()).optional(),
    }),
});

export const collections = {
    'activities': activitiesCollection,
    'profile': profileCollection,
};
